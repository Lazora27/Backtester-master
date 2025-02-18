import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AverageTrueRange': 1.0
        })
    )
