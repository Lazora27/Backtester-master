import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
