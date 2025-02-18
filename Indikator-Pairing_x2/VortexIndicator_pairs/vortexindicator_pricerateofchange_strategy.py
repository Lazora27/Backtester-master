import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
