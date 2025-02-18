import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
