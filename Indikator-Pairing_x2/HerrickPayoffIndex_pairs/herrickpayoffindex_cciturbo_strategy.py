import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
