import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
