import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'Fisher': 1.0
        })
    )
