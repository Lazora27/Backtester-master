import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'CCITurbo': 1.0
        })
    )
