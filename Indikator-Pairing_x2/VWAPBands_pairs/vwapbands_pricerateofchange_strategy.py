import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
