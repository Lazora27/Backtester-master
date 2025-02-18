import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
