import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'CyberCycle': 1.0
        })
    )
