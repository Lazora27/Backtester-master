import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
