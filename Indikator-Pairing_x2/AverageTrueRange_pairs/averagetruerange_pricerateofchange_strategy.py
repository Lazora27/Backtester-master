import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
