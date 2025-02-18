import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
