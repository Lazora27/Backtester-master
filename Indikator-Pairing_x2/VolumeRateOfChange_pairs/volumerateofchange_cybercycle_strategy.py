import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'CyberCycle': 1.0
        })
    )
