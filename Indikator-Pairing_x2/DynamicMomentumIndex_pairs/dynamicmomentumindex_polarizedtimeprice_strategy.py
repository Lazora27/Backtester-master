import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
