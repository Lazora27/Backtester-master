import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'MACDHistogram': 1.0
        })
    )
