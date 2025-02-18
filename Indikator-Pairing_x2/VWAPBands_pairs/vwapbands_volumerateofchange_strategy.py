import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
