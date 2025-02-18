import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
