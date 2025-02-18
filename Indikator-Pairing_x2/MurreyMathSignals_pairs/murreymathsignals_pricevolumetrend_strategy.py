import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
