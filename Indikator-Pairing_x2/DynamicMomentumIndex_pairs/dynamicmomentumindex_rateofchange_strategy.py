import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
