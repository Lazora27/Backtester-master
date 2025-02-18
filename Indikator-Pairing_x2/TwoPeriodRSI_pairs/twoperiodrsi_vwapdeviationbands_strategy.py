import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
