import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und GannAngles
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'GannAngles': 1.0
        })
    )
