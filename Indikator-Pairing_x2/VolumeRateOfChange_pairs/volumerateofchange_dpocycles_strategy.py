import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'DPOCycles': 1.0
        })
    )
