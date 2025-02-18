import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'AverageTrueRange': 1.0
        })
    )
