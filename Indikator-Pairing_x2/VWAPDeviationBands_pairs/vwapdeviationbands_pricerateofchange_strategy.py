import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
