import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'MassIndex': 1.0
        })
    )
