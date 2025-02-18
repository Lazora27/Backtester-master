import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MACDPredictor': 1.0
        })
    )
