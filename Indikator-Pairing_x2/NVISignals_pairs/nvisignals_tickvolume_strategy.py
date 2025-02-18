import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TickVolume
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TickVolume': 1.0
        })
    )
