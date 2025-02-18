import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
