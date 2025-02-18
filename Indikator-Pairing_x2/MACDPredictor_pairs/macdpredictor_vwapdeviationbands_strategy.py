import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
