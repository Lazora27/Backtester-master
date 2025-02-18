import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AverageTrueRange': 1.0
        })
    )
