import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
