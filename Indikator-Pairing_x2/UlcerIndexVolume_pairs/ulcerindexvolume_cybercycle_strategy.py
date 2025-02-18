import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und CyberCycle
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'CyberCycle': 1.0
        })
    )
