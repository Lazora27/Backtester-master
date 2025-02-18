import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
