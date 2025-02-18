import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AverageTrueRange': 1.0
        })
    )
