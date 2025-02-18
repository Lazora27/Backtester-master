import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und GannFans
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'GannFans': 1.0
        })
    )
