import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und GannFans
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'GannFans': 1.0
        })
    )
