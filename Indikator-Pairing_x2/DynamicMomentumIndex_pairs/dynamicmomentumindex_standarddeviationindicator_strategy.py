import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
