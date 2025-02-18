import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
