import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
