import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
