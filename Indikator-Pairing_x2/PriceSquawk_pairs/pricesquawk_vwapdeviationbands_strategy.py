import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
