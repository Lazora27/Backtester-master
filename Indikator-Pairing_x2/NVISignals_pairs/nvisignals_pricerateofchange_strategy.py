import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
