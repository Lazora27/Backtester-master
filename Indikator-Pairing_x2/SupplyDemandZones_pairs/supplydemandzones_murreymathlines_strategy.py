import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'MurreyMathLines': 1.0
        })
    )
