import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicSAR_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicSAR und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ParabolicSAR': 1.0,
            'AverageTrueRange': 1.0
        })
    )
