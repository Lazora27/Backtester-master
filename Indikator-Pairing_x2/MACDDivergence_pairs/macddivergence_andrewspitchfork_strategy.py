import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
