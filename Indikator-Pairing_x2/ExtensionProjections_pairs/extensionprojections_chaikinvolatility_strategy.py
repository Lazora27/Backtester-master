import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
