import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
