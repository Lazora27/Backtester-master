import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
