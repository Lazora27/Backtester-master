import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AverageTrueRange': 1.0
        })
    )
