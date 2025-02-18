import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'DonchianVolatility': 1.0
        })
    )
