import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
