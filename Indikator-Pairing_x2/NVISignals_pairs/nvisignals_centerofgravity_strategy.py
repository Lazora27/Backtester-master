import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CenterOfGravity': 1.0
        })
    )
