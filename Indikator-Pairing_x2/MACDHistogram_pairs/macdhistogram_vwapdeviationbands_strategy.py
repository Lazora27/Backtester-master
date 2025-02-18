import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
